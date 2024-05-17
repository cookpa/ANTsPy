
__all__ = ['compose_displacement_fields']

from ..core import ants_image_io as iio2
from ..core import ants_image as iio
from .. import utils
from ants.internal import get_lib_fn


def compose_displacement_fields(displacement_field, 
                                warping_field):
    """
    Compose displacement fields.

    Arguments
    ---------
    displacement_field : ANTsImage displacement field
        displacement field

    warping_field : ANTsImage displacement field
        warping field


    Example
    -------
    >>> import ants
    """

    libfn = get_lib_fn('composeDisplacementFieldsD%i' % displacement_field.dimension)
    comp_field = libfn(displacement_field.pointer, warping_field.pointer)

    new_image = iio2.from_pointer(comp_field).clone('float')
    return new_image


